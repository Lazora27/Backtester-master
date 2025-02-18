import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'ProjectionOscillator': 1.0
        })
    )

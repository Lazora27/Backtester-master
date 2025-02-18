import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'ProjectionBands': 1.0
        })
    )

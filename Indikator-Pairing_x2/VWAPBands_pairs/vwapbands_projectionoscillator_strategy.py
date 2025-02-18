import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'ProjectionOscillator': 1.0
        })
    )

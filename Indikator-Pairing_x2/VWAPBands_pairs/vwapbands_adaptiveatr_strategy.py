import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'AdaptiveATR': 1.0
        })
    )

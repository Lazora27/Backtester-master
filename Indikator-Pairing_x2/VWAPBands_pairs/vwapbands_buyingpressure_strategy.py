import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'BuyingPressure': 1.0
        })
    )

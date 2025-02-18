import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'BuyingPressure': 1.0
        })
    )

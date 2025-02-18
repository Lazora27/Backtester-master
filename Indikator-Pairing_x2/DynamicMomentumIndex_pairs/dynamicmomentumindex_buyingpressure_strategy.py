import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'BuyingPressure': 1.0
        })
    )

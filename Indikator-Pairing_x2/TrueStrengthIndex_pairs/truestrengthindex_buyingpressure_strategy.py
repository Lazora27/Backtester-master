import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'BuyingPressure': 1.0
        })
    )

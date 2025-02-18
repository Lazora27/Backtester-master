import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'BuyingPressure': 1.0
        })
    )

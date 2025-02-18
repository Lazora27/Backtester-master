import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und DPOCycles
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'DPOCycles': 1.0
        })
    )

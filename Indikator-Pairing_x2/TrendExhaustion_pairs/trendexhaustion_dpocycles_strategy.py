import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und DPOCycles
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'DPOCycles': 1.0
        })
    )

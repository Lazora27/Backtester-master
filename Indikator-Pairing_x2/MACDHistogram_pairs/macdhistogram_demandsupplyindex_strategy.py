import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )

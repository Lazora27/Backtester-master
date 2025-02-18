import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )

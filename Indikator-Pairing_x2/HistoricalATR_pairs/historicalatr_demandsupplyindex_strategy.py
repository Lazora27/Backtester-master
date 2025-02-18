import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )

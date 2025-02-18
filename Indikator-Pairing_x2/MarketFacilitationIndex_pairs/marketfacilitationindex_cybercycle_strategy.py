import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketFacilitationIndex_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketFacilitationIndex und CyberCycle
    """
    
    params = (
        ('indicators', {
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'MarketFacilitationIndex': 1.0,
            'CyberCycle': 1.0
        })
    )

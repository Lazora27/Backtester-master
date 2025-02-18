import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketFacilitationIndex_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketFacilitationIndex und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'MarketFacilitationIndex': 1.0,
            'WeeklyCycle': 1.0
        })
    )

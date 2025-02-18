import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketFacilitationIndex_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketFacilitationIndex und CCITurbo
    """
    
    params = (
        ('indicators', {
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'MarketFacilitationIndex': 1.0,
            'CCITurbo': 1.0
        })
    )

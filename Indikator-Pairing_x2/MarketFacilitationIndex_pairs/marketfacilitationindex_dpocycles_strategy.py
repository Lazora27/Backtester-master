import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketFacilitationIndex_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketFacilitationIndex und DPOCycles
    """
    
    params = (
        ('indicators', {
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'MarketFacilitationIndex': 1.0,
            'DPOCycles': 1.0
        })
    )

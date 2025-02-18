import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketFacilitationIndex_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketFacilitationIndex und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'MarketFacilitationIndex': 1.0,
            'BradleySiderograph': 1.0
        })
    )

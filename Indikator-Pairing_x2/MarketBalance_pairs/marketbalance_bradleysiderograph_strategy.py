import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketBalance_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketBalance und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'MarketBalance': 1.0,
            'BradleySiderograph': 1.0
        })
    )

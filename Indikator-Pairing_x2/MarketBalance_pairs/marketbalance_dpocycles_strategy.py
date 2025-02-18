import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketBalance_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketBalance und DPOCycles
    """
    
    params = (
        ('indicators', {
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'MarketBalance': 1.0,
            'DPOCycles': 1.0
        })
    )

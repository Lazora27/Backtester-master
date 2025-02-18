import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und TrendCycles
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'TrendCycles': 1.0
        })
    )

import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und MarketBalance
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'MarketBalance': 1.0
        })
    )

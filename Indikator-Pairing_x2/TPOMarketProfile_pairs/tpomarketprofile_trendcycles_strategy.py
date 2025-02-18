import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TPOMarketProfile_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TPOMarketProfile und TrendCycles
    """
    
    params = (
        ('indicators', {
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'TPOMarketProfile': 1.0,
            'TrendCycles': 1.0
        })
    )

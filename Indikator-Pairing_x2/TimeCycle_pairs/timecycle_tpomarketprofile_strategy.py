import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeCycle_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeCycle und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'TimeCycle': 1.0,
            'TPOMarketProfile': 1.0
        })
    )

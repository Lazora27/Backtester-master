import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'TPOMarketProfile': 1.0
        })
    )

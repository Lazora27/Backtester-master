import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'TPOMarketProfile': 1.0
        })
    )

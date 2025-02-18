import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CyberCycle_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CyberCycle und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'CyberCycle': 1.0,
            'TPOMarketProfile': 1.0
        })
    )

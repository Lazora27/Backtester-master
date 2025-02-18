import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'TPOMarketProfile': 1.0
        })
    )

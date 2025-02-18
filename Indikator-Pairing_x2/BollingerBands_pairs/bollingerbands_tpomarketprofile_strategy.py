import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'TPOMarketProfile': 1.0
        })
    )

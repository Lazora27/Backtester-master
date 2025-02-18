import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'TPOMarketProfile': 1.0
        })
    )

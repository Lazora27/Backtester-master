import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DPOCycles_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DPOCycles und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'DPOCycles': 1.0,
            'TPOMarketProfile': 1.0
        })
    )

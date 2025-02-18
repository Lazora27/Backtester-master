import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'TPOMarketProfile': 1.0
        })
    )

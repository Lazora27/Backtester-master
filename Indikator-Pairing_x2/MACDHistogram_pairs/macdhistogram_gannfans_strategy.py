import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und GannFans
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'GannFans': 1.0
        })
    )

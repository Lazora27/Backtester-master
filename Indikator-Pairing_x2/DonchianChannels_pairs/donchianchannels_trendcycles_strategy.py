import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und TrendCycles
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'TrendCycles': 1.0
        })
    )

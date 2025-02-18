import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )

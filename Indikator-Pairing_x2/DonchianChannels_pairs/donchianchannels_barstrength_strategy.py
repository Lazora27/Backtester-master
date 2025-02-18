import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und BarStrength
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'BarStrength': 1.0
        })
    )

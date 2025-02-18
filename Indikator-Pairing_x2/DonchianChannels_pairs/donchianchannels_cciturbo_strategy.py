import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und CCITurbo
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'CCITurbo': 1.0
        })
    )

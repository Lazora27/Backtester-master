import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'DonchianChannels': 1.0
        })
    )

import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'ParabolicSAR': 1.0
        })
    )

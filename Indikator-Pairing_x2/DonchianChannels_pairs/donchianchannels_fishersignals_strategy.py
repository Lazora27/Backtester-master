import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und FisherSignals
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'FisherSignals': 1.0
        })
    )

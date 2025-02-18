import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und FisherSignals
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'FisherSignals': 1.0
        })
    )

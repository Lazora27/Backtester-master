import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und FisherSignals
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'FisherSignals': 1.0
        })
    )

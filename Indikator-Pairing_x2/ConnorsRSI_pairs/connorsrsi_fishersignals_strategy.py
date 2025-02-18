import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und FisherSignals
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'FisherSignals': 1.0
        })
    )

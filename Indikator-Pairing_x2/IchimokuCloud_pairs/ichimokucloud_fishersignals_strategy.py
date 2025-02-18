import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und FisherSignals
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'FisherSignals': 1.0
        })
    )

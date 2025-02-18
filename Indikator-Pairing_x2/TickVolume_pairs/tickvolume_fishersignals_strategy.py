import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und FisherSignals
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'FisherSignals': 1.0
        })
    )

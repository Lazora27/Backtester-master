import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und FisherSignals
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'FisherSignals': 1.0
        })
    )

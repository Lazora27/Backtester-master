import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und CyberCycle
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'CyberCycle': 1.0
        })
    )

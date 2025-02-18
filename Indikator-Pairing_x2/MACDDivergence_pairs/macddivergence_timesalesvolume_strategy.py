import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'TimeSalesVolume': 1.0
        })
    )

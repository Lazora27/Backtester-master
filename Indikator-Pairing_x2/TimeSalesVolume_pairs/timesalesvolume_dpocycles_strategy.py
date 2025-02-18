import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und DPOCycles
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'DPOCycles': 1.0
        })
    )

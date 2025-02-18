import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )

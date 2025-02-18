import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndexVolume_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndexVolume und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'UlcerIndexVolume': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )

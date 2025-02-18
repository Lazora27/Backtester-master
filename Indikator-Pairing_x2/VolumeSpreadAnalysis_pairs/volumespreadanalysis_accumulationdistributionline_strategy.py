import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeSpreadAnalysis_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeSpreadAnalysis und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'VolumeSpreadAnalysis': {
                'class': VolumeSpreadAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeSpreadAnalysis'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'VolumeSpreadAnalysis': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )

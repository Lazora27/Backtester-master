import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )

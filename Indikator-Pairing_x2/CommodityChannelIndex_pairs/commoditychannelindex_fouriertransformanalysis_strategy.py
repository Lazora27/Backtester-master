import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
